pyinstaller --noconfirm src/main.py --noconsole --name="mDirt-2.1.2-windows" --add-data "src/ui.py:." --add-data "src/select_item.py:." --add-data "src/details.py:." --add-data "src/generation/v1_21_3/blocks.py:./generation/v1_21_3/" --add-data "src/generation/v1_21_3/items.py:./generation/v1_21_3/" --add-data "src/generation/v1_21_3/recipes.py:./generation/v1_21_3/" --add-data "src/generation/v1_21_4/blocks.py:./generation/v1_21_4/" --add-data "src/generation/v1_21_4/items.py:./generation/v1_21_4/" --add-data "src/generation/v1_21_4/recipes.py:./generation/v1_21_4/" --add-data "lib/1.21.3_data.json:./lib/" --add-data "lib/1.21.4_data.json:./lib/"