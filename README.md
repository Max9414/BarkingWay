# BaringWay

[Visit the Website Here](https://barkingway-bd2802e6d728.herokuapp.com/)

[Visit the Project's GitHub Repository Here](https://github.com/Max9414/BarkingWay)

![Responsive Image](documentation/amiresponsive.png)

## Introduction

Welcome to Barkingway, a FullStack website dedicated to events for dogs. The website presents pages dedicated to knowledge about breeds and pet-care and the main page, an event page where people can create and manage their events.
The purpose of this project was a build a full-stack site based around a business logic used to control a centrally-owned dataset. The technologies used for this project are HTML, CSS, JavaScript, Python, and Django.
The Database used was provided by code institute with PostgreSQL.

## UXD - User Experience Design

The user has been the cardinal point of my project, trying to take decisions that would facilitate both the readability and the positive experience of the user.

The planning of the project is broken into 5 planes:

- The Strategy Plane
- The Scope Plane
- The Structure Plane
- The Skeleton Plane
- The Surface Plane

---

## The Strategy Plane

### User stories

#### Homepage User stories

- As a visitor, I want to see a brief description of each page on the homepage so that I know where to find the information I need.
- As a visitor, I want to view the homepage so that I can learn about the site's purpose and the different pages available.

#### Pet-care page User stories

- As a visitor, I want to see detailed pet care tips so that I can follow expert advice for keeping my pets healthy.
- As a visitor, I want to view a list of pet care suggestions so that I can better care for my pets.

#### Breeds page User stories

- As a visitor, I want to click on a specific breed to see detailed information about it so that I can understand its characteristics and care needs.
- As a visitor, I want to view a list of different dog breeds so that I can learn about their key features.
- As a visitor, I want to be able to search dog breeds for keywords, so I can find breeds that suit my taste. (Used to create other search bars as well)

#### Registered user User stories

- As a registered user, I want to view my user profile page so that I can see my personal information and activities.
- As a registered user, I want to edit my profile information so that I can keep my details up to date.
- As a registered user, I want to add and view profiles of my owned dogs so that I can keep track of their information and share it with others.
- As a registered user, I want to upload pictures of my dogs to their profiles and modify their profiles, so that I can showcase them to the community.
- As a registered user, I want to delete a dog's profile in case of death for example.
- As a registered user, I want to view a list of upcoming dog-related events so that I can participate in activities and meet other dog owners.
- As a registered user, I want to log in so that I can access my personal dashboard and other member-only features.
- As a registered user, I want to log out so that I can secure my account when I'm done using the site.

#### General non User User stories

- As a visitor, I want to view a list of upcoming dog-related events so that I can decide to join the website if I'm interested.
- As a visitor, I want to register for an account so that I can access member-only features.

#### Superuser user stories

- As a superuser, I want to be able to manage the contents so that I can filter bad events or delete spam profiles.

#### Events page User stories

- As a registered user, I want to be able to join an event so that I can show my presence to the event creator and everyone who checks the event.
- As a registered user, I want to create an event for dog-related activities so that I can organize and invite others to participate.
- As a visitor, I want to view a list of upcoming dog-related events so that I can decide to join the website if I'm interested.
- As a registered user, I want to view a list of upcoming dog-related events so that I can participate in activities and meet other dog owners.

---

## The Scope Plane

The features designed for the project would have required a lengthy amount of time and a vast research of knowledge.\
Therefore I decided to take a phased deployment:

**Phase 1**

- Satisfy the must have user stories.
  - Homepage with clear pages description
  - Functional event page with CRUD functionalities
  - Pet-care and breeds page with article and pagination
  - Functional user page with CRUD functionalities

**Phase 2**

- Additional features
  - Research and filters bar
  - Filter to show only future events
  - Events created in the user page
  - Join/leave event checker

**Phase 3**

- Advanced features and feedbacks
  - api to create events directly on map
  - interaction with the dog profiles and more customizable events
  - users feedback for implementations

---

## The Structure Plane

#### Colors

![Colour pallete used for the project](documentation/colour_pallette.png)

I used warm colours for the body, containers and cards and contrasting them with dark cold colours for the text, creating a warm and contrasted easy to the eyes website.

#### Fonts

For the fonts I used Roboto, an easy and clear style. I opted for a single font to keep the design the same throughout the different pages.

#### Database design

(Upload design from tablet)

#### Key Models

**Owner**

- The owner profile has been linked to several other models to give the user as much clarity on their activities as possible
- The name field, the only necessary for the user page to work, is autogenerated when the User model is created through AllAuth.
- Its main relations are with Dog and Events

**Dog**

- The dog profile can be created through the user page.
- The model has been thought for future implementations, where events will be created with more customisable choices, to allow owners to join the correct events for their dogs.

**Event**

- The event model is the core of the project. People can create events adding important infos like location, date and time.
- The model is also used in connection with the user to display the created events in the user page
- It also has features to allow users to modify the number of participants, check if the user has joined already or not.

**Pet-care and Breed**

- These are the 2 standard models for static pages.
- These models are static and manageable only from the admin
- They have logic to allow research, allowing the user to find what they came for more rapidly

---

## The Skeleton Plane
