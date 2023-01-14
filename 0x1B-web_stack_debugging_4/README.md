# 0x1B.Web stack debugging #4
``DevOps`` ``SysAdmin`` ``Scripting`` ``Debugging``

| Task | File | Description |
|------|------|-------------|
testing how well the web server setup featuring Nginx is doing under pressure and applying a fix on the stack so that we get 0 request failed | [0-the_sky_is_the_limit_not.pp](./0-the_sky_is_the_limit_not.pp) | For the benchmarking, we are using ApacheBench which allows us simulate HTTP requests to a web server (remember when something is going wrong, logs are our best friends

Change the OS configuration so that it is possible to login with holberton user and open a file without any error message | [1-user-limit.pp](./1-user-limit.pp) | ensures no one is able to login as holberton
