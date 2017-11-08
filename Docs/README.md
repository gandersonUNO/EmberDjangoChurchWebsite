User Stores
===========

Website Visitor
---------------

-   As a website visitor, I want to view the home page so that I can get
    important information about the church.

    -   AC - Given a visitor, they can view static content on the home
        page

    -   AC – Given a visitor, they can view the page by visiting and

-   As a website visitor, I want to view the navigation items on every
    page so that I can browse the churches website.

    -   AC – Given a visitor, they can view the navigation items on
        every page

    -   AC – Given a visitor, they can go to the home page by pressing
        the home button on the nav bar

    -   AC – Given a visitor, they can go to the preschool page by
        pressing the preschool button on the nav bar

    -   AC – Given a visitor, they can go to the events page by pressing
        the events button on the nav bar

    -   AC – Given a visitor, they can go to the about page by pressing
        the about button on the nav bar

    -   AC – Given a visitor, they can go to the contact page by
        pressing the contact button on the nav bar

-   As a website visitor, I want to view a map with the address of the
    church in the footer of every page so that I can quickly determine
    the churches location

    -   AC - Given a visitor, they can view a google map on the footer
        of every page

-   As a website visitor, I want to view the past bulletins on every
    page so that I can find out what I missed on previous Sundays.

    -   AC – Given a visitor, they can view the past 5 weeks of
        bulletins with the weeks as the title on every page

    -   AC – Given a visitor, they can select any bulletin to bring up a
        pdf of that weeks bulletin on any page

    -   AC – Given a visitor, when clicking the view all link a new page
        will be displayed with every weeks bulletin with on any page

-   As a website visitor, I want to view a live Facebook feed of the
    church on every page so that I can get important updates about the
    community.

    -   AC – Given a visitor, they can get a live Facebook feed of the
        churches website on every page using a Facebook token

    -   AC – Given a visitor, they cannot see the Facebook feed if a
        Facebook feed token is missing

-   As a website visitor, I want to view a page with information
    regarding the preschool so that I can get important information
    about the preschool.

    -   AC - Given a visitor, they can view static content on the
        preschool page

    -   AC – Given a visitor, they can view the page by visiting
        /Preschool

-   As a website visitor, I want to view a page with a calendar for the
    preschool so that I can get upcoming events about the preschool.

    -   AC – Given a visitor, they can view a calendar with events with
        the What and When information

-   As a website visitor, I want to view a page with contact information
    for the preschool so that I can contact a member to enroll my child.

    -   AC – Given a visitor, they can view the contact information
        about the preschool

-   As a website visitor, I want to view a page with a calendar of
    upcoming events so that I can get an overview of upcoming events.

    -   AC - Given a visitor, they can view a calendar with events

    -   AC – Given a visitor, they can change the month of the events
        being displayed by either going forward or backwards

    -   AC – Given a visitor, they can view the current month when
        visiting the page

    -   AC – Given a visitor, they can view the What and When of events
        on the calendar

    -   AC – Given a visitor, they can view the page by visiting /Events

-   As a website visitor, I want to select an upcoming event on a
    calendar so that I can retrieve the What, When, Where, and Why of
    the event.

    -   AC – Given a visitor, they can click on an event on the churches
        event calendar will display a popup message box

    -   AC – Given a visitor, when viewing a message box, it contains
        the What, When, Where, Why of the event.

-   As a website visitor, I want to view an about page so that I can
    view the churches vison, mission statement and pastor’s information.

    -   AC - Given a visitor, they can view static content on the about
        page

    -   AC – Given a visitor, they can view the page by visiting

-   As a website visitor, I want to view a contact page so that I can
    know how to contact the church through email or phone.

    -   AC - Given a visitor, they can view static content on the
        contact page

    -   AC – Given a visitor, they can view the page by visiting

Website admin
-------------

-   As a website admin, I want to add/update/remove an event to the
    church calendar with the What, When, Where, and Why information so
    that visitors can know about upcoming events.

    -   AC- Given an admin, they can add a new event with the What,
        When, Where, and Why information.

    -   AC – Given an admin, they can remove an event

    -   AC – Given an admin, they can update an event

-   As a website admin, I want to add/update/remove an event to the
    preschool calendar with the What and when information so that
    visitors can know about upcoming preschool events.

    -   AC- Given an admin, they can add a new event with the What and
        When.

    -   AC – Given an admin, they can delete an event

    -   AC – Given an admin, they can update an event

-   As a website admin, I want to add/update/remove pdf bulletin files
    to the churches website so that users can view the bulletins.

    -   AC – Given an admin, they can upload a pdf with a date, and only
        a pdf

    -   AC – Given an admin, they can remove a bulletin

    -   AC – Given an admin, they can update the date and pdf of an
        entry

-   As a website admin, I want to add/update/remove the Facebook feed to
    the churches website by providing a read only token so that users
    can view live Facebook posts.

    -   AC – Given an admin, they can add a token for the Facebook feed

    -   AC – Given an admin, they can update the Facebook feeds token.

    -   AC – Given an admin, they can remove the Facebook feeds token.

-   As a website admin, I want to add/remove/update images to the home
    page by providing a URL or Image file so that I can change out the
    images on a seasonal or daily basis.

    -   AC – Given an admin, they can add an image to the home page by
        providing a URL or Image file

    -   AC – Given an admin, they can update an images URL or image
        file.

    -   AC – given an admin, they can remove an image URL or image file

-   As a website admin, I want to add/remove an alert notification to
    the home page with a start and end date/time, so that I can notify
    visitors about important information.

    -   AC – Given an admin, they can add an alert notification by
        providing a message, start date/time and end date/time

    -   AC – Given an admin, they can remove an alert notification

Misuse Stories
==============

-   As a hacker, I want to add/update/remove images so that I can infect
    user’s machines with viruses.

    -   Mitigation: require credentials to add/update/remove images

-   As a hacker, I want to add/update/remove upcoming church events so
    that I can infect user’s machines with viruses.

    -   Mitigation: require credentials to add/update/remove events

-   As a hacker, I want to add/update/remove upcoming preschool events
    so that I can infect user’s machines with viruses.

    -   Mitigation: require credentials to add/update/remove events

-   As a hacker, I want to add/update/remove bulletins so that I can
    infect user’s machines with viruses.

    -   Mitigation: require credentials to add/update/remove bulletins

-   As a hacker, I want to add/update/remove Facebook token so that I
    can infect user’s machines with viruses.

    -   Mitigation: require credentials to add/update/remove Facebook
        token

-   As a hacker, I want to add/update/remove alerts so that I can infect
    user’s machines with viruses.

    -   Mitigation: require credentials to add/update/remove alerts



