Title: Two Arguments Against Single-Page Applications
Date: 2015-11-15
Category: Software Engineering

Traditionally, websites work by re-loading and re-rendering the entire web page
for each request. Now that javascript is ubiquitous, it's possible to build
single-page applications. Instead of re-loading the page for each request,
javascript makes a request in the background, and then updates the page with the
results.

I'm neither for nor against single-page applications. There are projects where
single-page applications are perfect, and projects where they aren't. Here are
my two biggest concerns with single-page applications:

1.  **Code duplication.** You have to duplicate a lot of code and data modelling
    in order to make single-page applications secure. Say that you have a page
    with a configuration options form. When you click the submit button, your
    javascript code will check the options for validity, and if they're valid,
    send them up to PHP (or whatever server-side language you're using), where
    they have to be validated *again* and finally inserted into the database.
    You need the second validation, because the first validation happens
    client-side and can't be trusted.

    This problem isn't actually inherent to single-page applications. It's
    conceivable that a single-page app framework could have you represent the
    validation steps in one place, and then automatically generate server-side
    and client-side instances of that validity check. Maybe some frameworks
    already do this.

2.  **State destruction is useful.** In the traditional model, there's no state
    stored in the browser except for an identifying cookie. After each request,
    the client-side state is completely re-created from scratch. Constrast this
    with single-page applications, where one loaded page can have a lifetime of
    hours, not just minutes or seconds.

    The longer lifetime of single-page applications means there's more chance of
    bugs happening on the client side. Those errors could be silent or unhandled
    (as most unexpected javascript errors are), and the user might keep trying to
    use the application without realizing it's in an invalid state. Have you ever
    been using an online editor/whiteboard for 5 minutes, and then realized what
    you were writing/drawing wasn't getting sent to the server because of some
    error, and you lost all of that work? Constantly refreshing the page,
    although inefficient, resets the client to a valid state, so that it's much
    less likely for the client side to enter an invalid state.

    If you're going to have (non-security) bugs, it's helpful if they're on the
    server side. The environment is predictable since you created it, and you can
    debug it since you're in control of it.

These aren't reasons to reject single-page applications across the board.
They're just more things to think about when you're deciding if you want to use
a single-page application or not.

