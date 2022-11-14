# deactivate
# activate
# git init
# commit to repo     git satus    
# git add main.py--暫存區      
# git commit -m "add main.py"---進入commit
# public branch
print('hello')

# README.md 在gitHub直接顯示內容
# .gitignore 不會被追蹤

# pip install-requires----(裝錯了老師打錯字)
# pip freeze > requirments.txt
# pip install --heilp
# 移除套件 pip reinstall requires
# pip install --upgrade 更新
# pip install requests
# requests的功能是做http的連線


# web api openWeatherAPI  https://openweathermap.org/   
# lesson01.ipynb

import private
print(private.secret.open_weather_key)


# json解析器  online json viewer

print(__name__)

import datasource


def main():
    api_key = private.secret.open_weather_key
    city = datasource.get_forcase_data("Taipei", api_key)
    print(city)
    

if __name__ == "__main__":
    main()
