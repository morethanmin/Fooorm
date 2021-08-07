$(document).ready(function () {
  const csrftoken = $.cookie('csrftoken')

  $('.form-checkbox').on('input', function (e) {
    const checked = e.target.checked
    const id = e.target.dataset.id
    let checkedOptions = new Set()
    $('.fm-form-options')[0]
      .value.split(' ')
      .map((option) => checkedOptions.add(option))

    if (checked === true) checkedOptions.add(id)
    else checkedOptions.delete(id)
    checkedOptions.delete('')
    $('.fm-form-options')[0].value = [...checkedOptions].join(' ')
  })
})
