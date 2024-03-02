# get-domain-form-har
提取当前页面weby页面所有HTTP请求的domain
1. 使用谷歌浏览器或者火狐浏览器的dev工具，录制当前页面的网络请求，并获取HAR文件
<img src="/getHAR.png" alt="getHAR">
2. 修改当前python文件中HAR文件的路径
3. python解析当前文件即可获取domain列
<img src="/getDomain.png" alt="getDomain">
