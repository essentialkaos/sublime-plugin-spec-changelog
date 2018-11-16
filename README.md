## Spec Changelog Plugin

Simple plugin for Sublime Text 3 for adding changelog record header.

### Installation

1. Download the latest versions of `add_change_date.py` file;
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

[EKOL](https://essentialkaos.com/ekol)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
