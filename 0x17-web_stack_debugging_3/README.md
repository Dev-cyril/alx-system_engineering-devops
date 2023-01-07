# 0x17. Web stack debugging #3
``DevOps`` ``SysAdmin`` ``Scripting`` ``Debugging``

When debugging, sometimes logs are not enough. Either becuase the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack.

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites... It actually powers 26% of the web.
wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is very widely used set of tools.

| Task | File | Description |
|------|------|-------------|
Using ``strace``, find out why Apache is returning a 500 error | [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp) | file contains the code written as to debug the situation according to the task

