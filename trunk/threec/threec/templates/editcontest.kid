<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">

<head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
    <title>Edit A Contest</title>
</head>

<body>

  <form action="savecontest" method="post"> 
    Name:<textarea rows="1" name="name">${name}</textarea><br />
    Start:
    <select name="syear">
      <option value="2005">2005</option>
      <option value="2005">2006</option>
    </select>
    <select name="smonth" selected="11">
      <option py:for="x in range(12)" value="${x+1}">${x+1}</option>
    </select>
    <select name="sday">
      <option py:for="x in range(30)" value="${x+1}">${x+1}</option>
    </select>
    <select name="shour">
      <option py:for="x in range(24)" value="${x}">${x}</option>
    </select>
    <select name="smin">
      <option py:for="x in range(60)" value="${x}">${x}</option>
    </select>

    <br />End:
    <select name="eyear">
      <option value="2005">2005</option>
      <option value="2005">2006</option>
    </select>
    <select name="emonth">
      <option py:for="x in range(12)" value="${x+1}">${x+1}</option>
    </select>
    <select name="eday">
      <option py:for="x in range(30)" value="${x+1}">${x+1}</option>
    </select>
    <select name="ehour">
      <option py:for="x in range(24)" value="${x}">${x}</option>
    </select>
    <select name="emin">
      <option py:for="x in range(60)" value="${x}">${x}</option>
    </select>

    <input type="hidden" name="userId" value="${user}" />
    <br /><input type="submit" name="submit" value="Save"/> 
  </form>
  
  <table>
    <tr>
      <td>Problem</td><td>Remove</td>
    </tr>
    <hr />
    <tr py:for="prob in problemset">
      <td><a href="${prob.problemUrl}">${prob.problemName}</a></td>
      <td><a href="/remove?problem=${prob.id}">Remove</a></td>
    </tr>
  </table>
  
  <form action="addproblem" method="post">
    Name:<textarea rows="1" name="name"></textarea><br />
    Statement:<textarea rows="1" name="stmt"></textarea><br />
    Time Limit:<textarea rows="1" name="time">10</textarea><br />
    Memory Limit:<textarea rows="1" name="memory">100</textarea><br />
    Correctness:<textarea rows="1" name="correct">100</textarea><br />
    <input type="submit" name="submit" value="Add Problem to Contest"/>
  </form>

</body>
</html>
