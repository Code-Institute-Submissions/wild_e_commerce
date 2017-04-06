function displayNextImage()
    {
      x = (x === images.length - 1) ? 0 : x + 1;
      document.getElementById("img").src = images[x];
    }

    function displayPreviousImage()
    {
      x = (x <= 0) ? images.length - 1 : x - 1;
      document.getElementById("img").src = images[x];
    }

    function startTimer()
    {
      setInterval(displayNextImage, 3000);
    }

    var images = [], x = -1;
    images[0] = "images/header/6.jpg";
    images[1] = "images/header/2.jpg";
    images[2] = "images/header/3.jpg";
    images[3] = "images/header/5.jpg";
    images[4] = "images/header/ShopInterior1.jpg";