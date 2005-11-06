<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#">



<head>
  <title>Testing</title>
</head>

<body py:match="item.tag == '{http://www.w3.org/1999/xhtml}body'"> 

<?python
try:
   if message:
      pass
except NameError:
   print 'created an empty message'
   message = []

print 'this works'
print message
?>

  <span py:for="msg in message">
    <p py:content="msg">Message to be displayed</p>
  </span>
  <div py:replace="item[:]"> </div>
</body>
</html>
