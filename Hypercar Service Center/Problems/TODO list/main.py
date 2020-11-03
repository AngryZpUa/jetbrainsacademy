template = """
<html>
  <ul>
  {% for to_do in todos %}
    <li> {{ to_do }} </li>
  {% endfor %}
  </ul>
</html>
"""