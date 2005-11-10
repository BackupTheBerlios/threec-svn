<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">

<head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
    <title>Edit A Contest</title>
</head>

<body>

  <form action="savecontest" method="post"> 
    Name:<textarea name="name">${name}</textarea><br />
    Start:<br />End:<br />
    <input type="submit" name="submit" value="Save"/> 
  </form> 
  
  <table>
    <tr>
      <td>Problem</td><td>Remove</td>
    </tr>
    <tr py:for="prob in problemset">
      <td><a href="${prob.problemUrl}">${prob.problemName}</a></td>
      <td><a href="/remove?problem=${prob.id}">Remove</a></td>
    </tr>
    
    <form action="addproblem" method="post">
      Name:<textarea name="name"></textarea><br />
      Time Limit:<textarea name="time">10</textarea><br />
      Memory Limit:<textarea name="memory">100</textarea><br />
      Correctness:<textarea name="correct">100</textarea><br />
      <input type="submit" name="submit" value="Add Contest"/>
    </form>
  </table>
  
</body>
</html>
