<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#">

<head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
    <title>Your title goes here</title>
</head>

<body py:match="item.tag=='{http://www.w3.org/1999/xhtml}body'">
    <h1>TurboGears is Running</h1>
    
    <!-- <div py:if="turbogearsflash" class="flash" py:content="turbogearsflash"></div> !-->
    
    <div py:replace="item[:]"/>
</body>
</html>