# 【パスの結合・連結】
# Pythonではパスの結合や連結を行う関数が用意されています。プラットフォームに依存することなく安全にファイルパスを構築することができます。
# 
# 【os.path.join】
# パスを結合・連結するにはos.path.joinを使用します。引数はいくつでも指定できるため、8行目のように複数のパスを結合することもできます。
# 
# import os
# 
# 
# PROJECT_DIR = 'C:¥python-izm'
# SETTINGS_FILE = 'settings.ini'
# 
# print(os.path.join(PROJECT_DIR, SETTINGS_FILE))
# print(os.path.join(PROJECT_DIR, 'settings_dir', SETTINGS_FILE))
# 
# 
# 《実行結果》
# C:¥python-izm¥settings.ini
# C:¥python-izm¥settings_dir¥settings.ini
# 
# 上記はWindowsでの実行結果ですが、LinuxやMac OSなどでもそのプラットフォームに応じたファイルセパレータ（ / ）を用いてパスが構築されます。ファイルセパレータを取得するにはセパレータの取得を参照してください。(https://www.python-izm.com/advanced/separator/)
# 
# 
