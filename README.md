# py-mealdb ![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/sherwin-14/py-mealdb/tests.yml) ![PyPI - Version](https://img.shields.io/pypi/v/py-mealdb) [![License: LGPL v3](https://img.shields.io/badge/License-LGPL_v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0) ![GitHub Repo stars](https://img.shields.io/github/stars/Sherwin-14/py-mealdb) ![PyPI - Downloads](https://img.shields.io/pypi/dm/py-mealdb)


py-mealdb is a Python library that allows users to interact effortlessly with TheMealDB API, providing access to a vast collection of meal recipes, ingredients, and culinary inspiration from around the world.

## 📚 Table of Contents

1. [Installation](#-installation) 
2. [Quick Start](#️-quick-start) 
3. [Documentation](#-documentation) 📄
4. [Contributing](#-contributing) 🤝
5. [License](#-license) 📜
6. [Code of Conduct](#-code-of-conduct) 🚫

## 💻 Installation

```py
pip install py-mealdb
```

## 🏃‍♂️ Quick Start

```py
from mealdb import MealDB

mb = MealDB(API_KEY)
meal = mb.get_meal_by_name('Potato Salad')

print(meal)
```

## 🤝 Contributing
If you'd like to contribute to the package, please submit a pull request or report an issue on the issue tracker.

## 📄 Documentation
For more information, please refer to our [Documentation](https://sherwin-14.github.io/py-mealdb/).

## 🚫 Code of Conduct
For more information about code of conduct click here [Conduct](https://github.com/Sherwin-14/py-mealdb/blob/main/CODE_OF_CONDUCT.md).

## 📜 License
This project is licensed under the CC-BY-NC-SA-4.0
