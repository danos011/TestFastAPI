from enum import Enum


class ProductsCategory(str, Enum):
    building_materials = "Стройматериалы"
    electronics = "Электроника"
    household_goods = "Хозтовары"
