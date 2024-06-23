# Установка проекта

## Requirements

* Python >= 3.11.4
* Poetry

## Как установить питон

### Устанавливаем Питон 3.11.9

Пример установки `pyenv` на MacOS

```shell
brew install pyenv
pyenv install 3.11.9
# Optional. Select 3.11.9 as global python version
pyenv global 3.11.9
# Or set local version in project directory
pyenv local 3.11.9
```

### Устанавливаем Poetry

```shell
curl -sSL https://install.python-poetry.org | python3 -

# for zsh
poetry completions zsh > ~/.zfunc/_poetry
# and add to .zshrc
fpath+=~/.zfunc
autoload -Uz compinit && compinit

# for bash
poetry completions bash >> ~/.bash_completion

# for Oh My Zsh
mkdir $ZSH_CUSTOM/plugins/poetry
poetry completions zsh > $ZSH_CUSTOM/plugins/poetry/_poetry
# You must then add poetry to your plugins array in ~/.zshrc:
plugins(
  poetry
  ...
)
```

---

### Устанавливаем зависимости

```shell
poetry init
```

### Запуск программы

1. Скопируйте из .env.example все в .env file

```shell
cp .env.example .env
```

2.  В .env file поменяйте путь до бд(Дамп бд приложил вместе с проектом)

> **DATABASE_URL** – your postgreSQL DSN
