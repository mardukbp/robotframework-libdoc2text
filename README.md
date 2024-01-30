# libdoc2text

Generate library documentation in plain text from the JSON generated by libdoc.

## Use Cases

- Markdown documentation to generate a static site with Mkdocs or upload it to Confluence
- Asciidoc documentation to generate a static site with Asciidoctor

## How to use it

1. Install the package

```bash
pip install robotframework-libdoc2text
```

2. Save the desired template to the current directory

For Markdown:

```bash
libdoc2text init.md
```

For Asciidoc:

```bash
libdoc2text init.adoc
```

**Hint**: In case your environment does not allow executing libdoc2text, call the Python module directly:

```bash
python -m Libdoc2Text init.md
```

3. Modify the template

4. Generate the library documentation with libdoc

```bash
python -m robot.libdoc Library Library.json
```

5. Generate the plain text documentation with libdoc2text

```bash
libdoc2text run library.md.jinja Library.json Library.md
```

## How it works

The template files are Jinja templates. When `libdoc2text run` is executed Jinja processes the template, which results in a Markdown or Asciidoc file.
