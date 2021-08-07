$(document).ready(function () {
  const csrftoken = $.cookie('csrftoken')
  let currentPosition = parseInt($('.fm-quickmenu').css('top'))
  $(window).scroll(function () {
    let position = $(window).scrollTop()
    $('.fm-quickmenu')
      .stop()
      .animate({ top: position + currentPosition + 'px' }, 500)
  })

  //update form input
  $('.form-input').on('input', function (e) {
    // form >> key, name, title, description, questions
    const { key } = e.target.dataset
    const name = e.target.name
    const value = e.target.value

    fetch(`/api/form`, {
      method: 'PUT',
      headers: { 'X-CSRFToken': csrftoken },
      body: JSON.stringify({
        key,
        name,
        value,
      }),
    })
      .then((response) => response.json())
      .then((result) => {})
  })

  //delete form
  $('.fm-quickmenu-delete').click(function (e) {
    const { form_key } = e.target.dataset
    fetch(`/api/form`, {
      method: 'DELETE',
      headers: { 'X-CSRFToken': csrftoken },
      body: JSON.stringify({
        form_key: form_key,
      }),
    })
      .then((response) => response.json())
      .then((result) => {
        window.location = `/forms`
      })
  })
  //add question
  $('.fm-quickmenu-add').click(function (e) {
    const { form_key } = e.target.dataset
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

  // update question input
  $('.question-input').on('input', function (e) {
    const { id, form_key } = e.target.dataset
    const name = e.target.name
    const value = e.target.value
    fetch(`/api/question/${id}`, {
      method: 'PUT',
      headers: { 'X-CSRFToken': csrftoken },
      body: JSON.stringify({
        name,
        value,
      }),
    })
      .then((response) => response.json())
      .then((result) => {
        //html 삽입 예정
        if (name === 'type') window.location = `/forms/${form_key}/edit`
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

  // add option
  $('.fm-type-option-add').click(function (e) {
    const { id, form_key } = e.target.dataset
    fetch(`/api/option`, {
      method: 'POST',
      headers: { 'X-CSRFToken': csrftoken },
      body: JSON.stringify({
        id: id, //question id
        name: '새로운 명',
      }),
    })
      .then((response) => response.json())
      .then((result) => {
        //html 삽입 예정
        window.location = `/forms/${form_key}/edit`
      })
  })

  // update option input
  $('.option-input').on('input', function (e) {
    const { id } = e.target.dataset
    const name = e.target.name
    const value = e.target.value
    fetch(`/api/option/${id}`, {
      method: 'PUT',
      headers: { 'X-CSRFToken': csrftoken },
      body: JSON.stringify({
        name,
        value,
      }),
    })
      .then((response) => response.json())
      .then((result) => {})
  })

  // delete option
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

  $('.fm-quickmenu-share').click(function (e) {
    const t = document.createElement('textarea')
    document.body.appendChild(t)
    t.value = window.document.location.href.slice(0, -5)
    t.select()
    document.execCommand('copy')
    document.body.removeChild(t)
    toastr.success('클립보드에 저장되었습니다.')
  })
})
// toastr.success('저장에 성공하였습니다.')
