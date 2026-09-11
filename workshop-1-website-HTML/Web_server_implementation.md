## Notes about Workshop 1

In the following section I'm going to detail the step by step implmentation of the workshop and the pathline that I followed to solve the problem.


### Set up the resolution name for `workshop1.webapp`
The first step was make the repository in github to have a version control into the project.


I need to set up the `hosts` int he both sides:
- In my windows machine (client)
- In the WSL which the server runs

I ran the following command:
```bash
ping -c 3 workshop1.webapp
```

To test if in the both sides the name is recognized by the machine.


### Set up the Apache server

The first step is test if the `80` port is free with the following command:
```bash
sudo ss -tlnp | grep ':80'
```

If the port ``80`` is free, we can continue and install the apache server with the following command:
```bash
sudo apt-get update
sudo apt-get install apache2
```

After the installation of `apache2`, we have to initialize the service (daemon) with the following command:
> Definition of a service: A background process or processes that handles system requests or tasks.
```bash
sudo systemctl start apache2
```

Now, we can verify that the server is running with the following command:
```bash
sudo systemctl status apache2
```

> **Important Note:** In case of we shut down the machine which acts with the web server ``(Apache2)``, we have to initialize the service again with the command ``sudo systemctl start apache2``.

We can test that the Apache service it works with the following testing command:
```bash
curl -I http://localhost
```
If we saw an ``HTTP/1.1 200 OK`` response, everithing is ok!

Opening `http://localhost` in the Windows browser shows the default
Ubuntu/Apache page. This proves Windows can reach a service running
inside WSL. The path is:

- The browser on Windows connects to `127.0.0.1:80`.
- WSL2 runs as a lightweight VM with its own network stack. Windows
  performs localhost forwarding: it relays the connection to port 80
  inside the WSL VM.
- Inside WSL, the Linux kernel delivers the connection to whichever
  process is bound to port 80 — the Apache daemon (a background
  process that waits for and serves web requests).
- Apache reads the request, resolves it to a file on disk, and returns
  the response back along the same path.

After deploy the apache server, I tested enter on the web browser the url `http://workshop1.webapp`, however the browser can't resolve the name.

The problem is that windows recognize only the request with `ipv6`, but by default when we type `127.0.0.1` or `workshop1.webapp` the request is made with `ipv4`. So we need to configure in windows making a new file into the User path a `.wslconfig` file which incude:
```ini
[wsl2]
networkingMode=mirrored
```
> **Note:** In mirrored mode, WSL 2 directly shares and mirrors the Windows host's network settings and interfaces.


With problem fixed, we have to create the configuration file in `sites-available` folder.

```bash
sudo nano /etc/apache2/sites-available/workshop1.webapp.conf
```

The contents of the file are shown below
```text
<VirtualHost *:80>
    ServerName workshop1.webapp
    DocumentRoot /mnt/c/Users/Usuario/Documents/YachayTech/Eigth_semester/web_applications/Web-applications-course-Yachay-Tech/workshop-1-website-HTML
</VirtualHost>

```

After we define the configuration file, we have to test first if the apaache configuration works, with the following testing command:

```bash
sudo apache2ctl configtest
```

If the configuration is ok, we have to enable the site with the following command:

```bash
sudo a2ensite workshop1.webapp.conf
```

After we enable the site, we have to restart the apache service with the following command:

```bash
sudo systemctl restart apache2
```

With the execution of each commands, we enter to `http://workshop1.webapp` in the browser, 
and we see the following result:

```log
[Sun Aug 23 11:47:46.636368 2026] [authz_core:error] [pid 15494:tid 133215988094656] [client 127.0.0.1:59460] AH01630: client denied by server configuration: /mnt/c/Users/Usuario/Documents/YachayTech/Eigth_semester/web_applications/Web-applications-course-Yachay-Tech/workshop-1-website-HTML/
```

The root of the problem, is that we dont configure the permissions on the config file, for that the client can't access. For solving the problem we must to add the `<Directory>` into `<VirtualHost>` directive in the config file.
```text
<Directory /mnt/c/Users/Usuario/Documents/YachayTech/Eigth_semester/web_applications/Web-applications-course-Yachay-Tech/workshop-1-website-HTML>
    Require all granted
</Directory>
```

Now we test the config file with the following testing command:

```bash
sudo apache2ctl configtest
```

If the result is ``Syntax OK``, we can continue restarting the apache server:

```bash
sudo systemctl restart apache2
```

Now we can enter to ``http://workshop1.webapp`` in the browser and it works. We see the content of the ``index.html`` file. Our server is running successfully! :\)

The next steps correspond to the activities using HTML for creating the web page using the configured `apache2` server.


## Notes about HTML implementation on the activity






---
#### Questions
1. Cómo un servidor web atiende muchas solicitudes a la vez? Si apache abre un hilo por cada petición solicitada al servidor
2. Cómo pueden vivir diferentes páginas web en una misma máquina que usa la misma dirección IP?

