"""Focused regression cases against temporary copies of the real bundle."""

import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

import yaml


SCRIPT = Path(__file__).with_name("validate-docs.py")
SPEC = importlib.util.spec_from_file_location("validate_docs", SCRIPT)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class DocumentationContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.bundle = Path(self.temp.name) / "docs"
        shutil.copytree(SCRIPT.parent.parent / "docs", self.bundle)

    def errors(self):
        return validator.validate(self.bundle)[0]

    def change_metadata(self, relative, change):
        path = self.bundle / relative
        _, metadata, body = validator.frontmatter(path.read_text(), path, [])
        change(metadata)
        path.write_text("---\n" + yaml.safe_dump(metadata, sort_keys=False) + "---\n" + body)

    def append(self, relative, text):
        path = self.bundle / relative
        path.write_text(path.read_text() + text)

    def test_migrated_bundle_and_area_entries(self):
        self.assertEqual([], self.errors())

    def test_malformed_yaml(self):
        path = self.bundle / "README.md"
        path.write_text("---\ntype: [broken\n---\n# Broken\n")
        self.assertIn("malformed YAML", "\n".join(self.errors()))

    def test_missing_or_invalid_type(self):
        for value in (None, "", "   ", 42):
            with self.subTest(value=value):
                self.change_metadata("README.md", lambda m: m.update(type=value))
                self.assertIn("type must be a non-empty string", "\n".join(self.errors()))
        self.change_metadata("README.md", lambda m: m.pop("type"))
        self.assertIn("type must be a non-empty string", "\n".join(self.errors()))

    def test_adopted_metadata_conventions(self):
        path = self.bundle / "README.md"
        original = path.read_text()
        for field, value in (("title", ""), ("description", 2), ("tags", "docs"),
                             ("tags", ["has space"]), ("tags", ["123"]), ("tags", [])):
            with self.subTest(field=field, value=value):
                path.write_text(original)
                self.change_metadata("README.md", lambda m: m.update({field: value}))
                self.assertIn(f"concept {field}", "\n".join(self.errors()))

    def test_nested_index_frontmatter(self):
        path = self.bundle / "process/index.md"
        path.write_text('---\nokf_version: "0.2"\n---\n' + path.read_text())
        self.assertIn("nested indexes must not have frontmatter", "\n".join(self.errors()))

    def test_root_version_contract(self):
        for metadata in ({"okf_version": "0.1"}, {"okf_version": 0.2},
                         {"okf_version": "0.2", "title": "Not a concept"}):
            with self.subTest(metadata=metadata):
                self.change_metadata("index.md", lambda m: (m.clear(), m.update(metadata)))
                self.assertIn("root frontmatter", "\n".join(self.errors()))

    def test_broken_navigation_target(self):
        path = self.bundle / "index.md"
        path.write_text(path.read_text().replace("(process/index.md)", "(missing/index.md)"))
        self.assertIn("missing local file target: missing/index.md", "\n".join(self.errors()))

    def test_description_and_tag_drift(self):
        for field, value in (("description", "Changed scope."), ("tags", ["changed"])):
            with self.subTest(field=field):
                self.change_metadata("README.md", lambda m: m.update({field: value}))
                self.assertIn(f"{field} projection drift", "\n".join(self.errors()))

    def test_wrapping_formatting_tag_order_and_extensions(self):
        self.change_metadata("README.md", lambda m: m.update(
            description=m["description"].replace(" ", "\n"),
            tags=list(reversed(m["tags"])), custom_extension={"preserved": True},
        ))
        path = self.bundle / "index.md"
        path.write_text(path.read_text().replace("Human entrypoint", "**Human**\n  entrypoint")
                        .replace("mental model", "mental\n  model"))
        self.assertEqual([], self.errors())

    def test_routing_hint_required(self):
        path = self.bundle / "index.md"
        path.write_text(path.read_text().replace("**Read when:**", "**Missing label:**", 1))
        self.assertIn("expected description, Read when, and Tags", "\n".join(self.errors()))

    def test_concept_and_child_area_coverage(self):
        # A new concept is not silently accepted just because its metadata is valid.
        shutil.copy(self.bundle / "README.md", self.bundle / "extra.md")
        self.assertIn("missing discovery entry for extra.md", "\n".join(self.errors()))
        (self.bundle / "extra.md").unlink()
        # A new area needs discovery in its parent, independently of concept metadata.
        shutil.copytree(self.bundle / "process", self.bundle / "another-area")
        self.assertIn("missing discovery entry for another-area/index.md", "\n".join(self.errors()))

    def test_actual_links_and_fragments_only(self):
        self.append("README.md", """

`[Inline example](missing-inline.md)`

```markdown
[Fenced example](missing-fenced.md)
```

    [Indented example](missing-indented.md)

[External](https://example.org/missing.md#anything)
[Email](mailto:docs@example.org)
[Reference link][dictionary]

[dictionary]: DICTIONARY.md#global-docs
""")
        self.assertEqual([], self.errors())
        self.append("README.md", "\n[Missing heading](DICTIONARY.md#no-such-heading)\n")
        self.assertIn("missing heading fragment", "\n".join(self.errors()))
        self.append("README.md", "\n[Broken reference][broken]\n\n[broken]: absent.md\n")
        self.assertIn("missing local file target: absent.md", "\n".join(self.errors()))


if __name__ == "__main__":
    unittest.main()
