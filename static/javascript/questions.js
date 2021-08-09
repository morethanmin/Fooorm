$(function () {
  $(`.fq-1`).show()
  let options = $('.fq-option')
  let inputs = $('.fq-input')
  value = inputs.map(function () {
    return this.value
      .slice(1, -1)
      .split(/,\s?/)
      .map((v) => parseInt(v))
  })
  options.map(function () {
    const targetId = this.id
  })

  console.log(value)

  $('.fq-select').on('input', function (e) {
    selectedValue = $('.fq-select option:selected').val()
    $(`.fq-box`).hide()
    $(`.fq-${selectedValue}`).show()
  })
})
