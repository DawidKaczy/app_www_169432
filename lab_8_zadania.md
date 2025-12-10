{
  postsByTitlePhrase(phrase: "Pierwszy post") {
    id
    title
  }
}
odpowiedź:
{
  "data": {
    "postsByTitlePhrase": [
      {
        "id": "4",
        "title": "Pierwszy post"
      },
      {
        "id": "3",
        "title": "Pierwszy post"
      }
    ]
  }
}

{
  countPostsByUser(userId: 1)
}
odpowiedź:
{
  "data": {
    "countPostsByUser": 5
  }
}



{
  topicsByCategoryName(name: "Python") {
    id
    name
  }
}
odpowiedź:
{
  "data": {
    "topicsByCategoryName": [
      {
        "id": "3",
        "name": "Django REST Framework"
      },
      {
        "id": "4",
        "name": "Kolorowy"
      },
      {
        "id": "5",
        "name": "Wielka stopa"
      }
    ]
  }
}


mutation {
  createPost(
    title: "Nowy"
    text: "Test"
    topicId: 1
    slug: "nowe-graphql"
  ) {
    post {
      id
      title
      }
    }
  }

odpowiedź:
{
  "data": {
    "createPost": {
      "post": {
        "id": "9",
        "title": "Nowy"
      }
    }
  }
}