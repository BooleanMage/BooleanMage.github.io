---
layout: page
title: Contact
permalink: /Contact/
redirect_from:
  - /contact/
---

<style>
  .contact-form {
      max-width: 100%;
  }

  .contact-form input[type="text"],
  .contact-form input[type="email"],
  .contact-form textarea {
      width: 100%;
  }

  .contact-form textarea {
      height: 200px;
  }

</style>

{% include social.html %}

<form action="https://formspree.io/f/mwkgvjql" method="POST" class="contact-form">
    <label for="name">What's your name/id?:</label><br>
    <input type="text" id="name" name="name" required><br>
    <label for="email">Your email address?:</label><br>
    <input type="email" id="email" name="_replyto" required><br>
    <label for="message">Anything want to say?:</label><br>
    <textarea id="message" name="message" required></textarea><br>
    <input type="submit" value="Submit"> <p align="right"><i>powered by formspree service</i></p><br>
</form>