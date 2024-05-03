import requests

url = 'http://apis.data.go.kr/1390802/AgriFood/FdFoodCkryImage/getKoreanFoodFdFoodCkryImageList'
params ={'serviceKey' : 'YV8OhM3PmYs8nZRYBGLvcJ3c%2Bl3I13ySsOnUgSm4N1y5sae29L3T3cdo3E8hty%2FooLqQUATTLzf2jxnOpuP15w%3D%3D', 
         'service_Type' : 'xml', 'Page_No' : '1', 'Page_Size' : '20', 'food_Name' : '밥', 'ckry_Name' : '조리' }

response = requests.get(url, params=params)
print(response.content)