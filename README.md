# dorker
Automatik search engine dorking tool

## Installation

#### pipx
```sh
pipx install git+https://github.com/winter1245/dorker
```
#### Example file .dorker/pattern.txt
```sh
google site:TARGET.com filetype:pdf
github org:TARGET "password" type=code
```

#### Usage

```sh
dorker -h
dorker searchterm pattern pattern2
```
