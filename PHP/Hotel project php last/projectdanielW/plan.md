<style>
   body
   {background-color: #012;}
   h1
   { 
    color: #3dd;
    font-size:3.5rem
   }
   h2
   {

    font-size: 2.5rem;
    color : #0fa;
   }
   h3
   {

    font-size: 2rem;
    color : #9af;
   }

   h4 {
      font-size: 1.5rem;
      color: #4f7;
   }
</style>



## hirachie

### includes
- _init.inc.php (überall)
    - functions.inc.php
    - pdo-connect.inc.php
- _header.inc.php (überall)



### sites
- index.php
    - details.php (nicht in nav)
    - login.php (nur ausgeloggt )  
    - logout.php (nur eingelogt)
    - register.php (nur ausgeloggt )
    - requests.php (nur admin)

---------------------------------------