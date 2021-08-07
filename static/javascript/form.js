$(document).ready(function () {
  const csrftoken = $.cookie('csrftoken')
  let currentPosition = parseInt($('.fm-quickmenu').css('top'))
  $(window).scroll(function () {
    let position = $(window).scrollTop()
    $('.fm-quickmenu')
      .stop()
      .animate({ top: position + currentPosition + 'px' }, 500)
  })

  // change question type
  $('.fm-form-select').on('input', function (e) {
    const { key, form_key } = e.target.dataset
    const type = e.target.value
    fetch(`/api/question/${key}`, {
      method: 'PUT',
      headers: { 'X-CSRFToken': csrftoken },
      body: JSON.stringify({
        form_key: form_key,
        name: '새로운 질문',
        type: type,
        required: false,
      }),
    })
      .then((response) => response.json())
      .then((result) => {
        //html 삽입 예정
        window.location = `/forms/${form_key}/edit`
      })
  })

  //add question
  $('.fm-quickmenu-add').click(function (e) {
    const { form_key } = e.target.dataset
    const type = e.target.value
    fetch(`/api/question`, {
      method: 'POST',
      headers: { 'X-CSRFToken': csrftoken },
      body: JSON.stringify({
        form_key: form_key,
      }),
    })
      .then((response) => response.json())
      .then((result) => {
        //html 삽입 예정
        window.location = `/forms/${form_key}/edit`
      })
  })

  //delete question

  $('.fm-form-centent-bottom-trash').click(function (e) {
    const { id, form_key } = e.target.dataset
    fetch(`/api/question/${id}`, {
      method: 'DELETE',
      headers: { 'X-CSRFToken': csrftoken },
    })
      .then((response) => response.json())
      .then((result) => {
        //html 삽입 예정
        window.location = `/forms/${form_key}/edit`
      })
  })

  // add question option
  $('.fm-type-option-add').click(function (e) {
    const { id, form_key } = e.target.dataset
    console.log(id, form_key)
    fetch(`/api/option`, {
      method: 'POST',
      headers: { 'X-CSRFToken': csrftoken },
      body: JSON.stringify({
        id: id,
        name: '새로운 옵션',
      }),
    })
      .then((response) => response.json())
      .then((result) => {
        //html 삽입 예정
        window.location = `/forms/${form_key}/edit`
      })
  })

  // delete question option
  $('.fm-type-option-btns').click(function (e) {
    const { id, form_key } = e.target.dataset

    fetch(`/api/option/${id}`, {
      method: 'DELETE',
      headers: { 'X-CSRFToken': csrftoken },
    })
      .then((response) => response.json())
      .then((result) => {
        //html 삽입 예정
        window.location = `/forms/${form_key}/edit`
      })
  })
})
// toastr.success('저장에 성공하였습니다.')
