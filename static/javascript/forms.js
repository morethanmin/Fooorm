$(function () {
  console.log('loaded')

  $('#fs-add').click(function (e) {
    const csrftoken = $.cookie('csrftoken')
    fetch('/forms/add', {
      method: 'POST',
      headers: { 'X-CSRFToken': csrftoken },
      body: JSON.stringify({
        name: '새로운 설문지',
      }),
    })
      .then((response) => response.json())
      .then((result) => {
        window.location = `/forms/${result.key}/edit`
      })
  })
})
