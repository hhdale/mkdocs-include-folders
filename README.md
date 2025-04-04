# Folder include plugin for mkdocs

<!--This repo was forked from [mkdocs-include](https://github.com/RedisLabs/mkdocs-include) plugin.-->

`mkdocs-include-folders` is a
[mkdocs plugin](http://www.mkdocs.org/user-guide/plugins/) that allows you
to include and prioritize folders from your input. 

## Quick start

1. Install the module using pip: `pip3 install mkdocs-include-folders`

2. If your document folders look like this:
```
documents
   project1
      mkdocs.yml
      specifications.md
   project2
      mkdocs.yml
      specfications.md
   shared-docs
      introduction.md
      contact.md
      .....
```
you may want to create a document including pages from the ``project1`` and ``shared-docs`` and present them in the same folder, this plugin will take documents from ``project1`` and ``shared-docs`` and place the im the same folder and also proritize files in ``project1`` over files in ``shered-docs`` if they have the same name.
   
3. In your project, add a plugin configuration to `mkdocs.yml`:
   ```yaml
   docs_dir: ..
   plugins:
      - include-folders
   ```
   or
   ```yaml
   docs_dir: ..
   plugins:
     - include-folders:
         priority_path:
           - 'project1/*'
           - 'shared-docs/*'
   ```

You can provide one or more patterns.  (If you don't provide any patterns, 
then nothing will happen!)

Note!  Because of peculiarity of yaml syntax, the `glob:` and `regex:` lines
**must not** start with a dash, but the lines under them **must** start with
a dash.

Also because of yaml, patterns that start with a punctuation mark must be
quoted.

When writing regexes, it's best to use single quotes rather than double
quotes, so that your regex backslash escapes are preserved correctly without
having to be doubled up.
