## Spec Changelog Plugin [![codebeat badge](https://codebeat.co/badges/bce2e63a-1ae7-4a31-8fed-3af4d751f4f4)](https://codebeat.co/projects/github-com-essentialkaos-sublime-plugin-spec-changelog-master) [![License](https://gh.kaos.st/apache2.svg)](https://www.apache.org/licenses/LICENSE-2.0)

Simple plugin for Sublime Text 3 for adding changelog record header.

### Installation

1. Download the latest versions of `add_change_date.py` file;
```bash
cd "~/Library/Application\ Support/Sublime\ Text\ 3/Packages/"
wget https://kaos.sh/sublime-plugin-spec-changelog/add_change_date.py
# or
curl https://kaos.sh/sublime-plugin-spec-changelog/add_change_date.py -o "~/Library/Application\ Support/Sublime\ Text\ 3/Packages/add_change_date.py"
```
2. Copy it into directory `Sublime Text 3/Packages/User/`;
3. Go to _Preferences_ → _Settings_;
4. Add `spec_author_name` and `spec_author_mail` properties;
5. Go to _Preferences_ → _Key Bindings_;
6. Add something like this:
```json
[
  {"keys": ["ctrl+0"], "command": "prompt_add_change_date" }
]
```
7. Press <kbd>Ctrl</kbd>+<kbd>0</kbd> in your changelog section.

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
