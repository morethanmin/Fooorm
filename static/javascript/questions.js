$(function () {
  $(`.fq-1`).show()

  $('.fq-select').on('input', function (e) {
    selectedValue = $('.fq-select option:selected').val()
    $(`.fq-box`).hide()
    $(`.fq-${selectedValue}`).show()
  })
})
