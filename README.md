# mkdocs-include-folders
# Folder include plugin for mkdocs

This repo was forked from [mkdocs-include](https://github.com/RedisLabs/mkdocs-include) plugin.

`mkdocs-include-folder` is a
[mkdocs plugin](http://www.mkdocs.org/user-guide/plugins/) that allows you
to include and prioritize folders from your input. 

## Quick start

1. Install the module using pip: `pip3 install mkdocs-include-folders`

2. In your project, add a plugin configuration to `mkdocs.yml`:
   ```yaml
   plugins:
      - include-folders
   ```
   or
   ```yaml
   plugins:
     - include-folders:
         priority_path:
           - 'specific-docs/*'
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
