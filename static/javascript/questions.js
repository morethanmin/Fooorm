$(function () {
  $(`.fq-1`).show()
  Inputs = $('.fm-pieVal')
  Inputs.map(function (i) {
    //labels
    let labels = this.value
      .slice(1, -1)
      .split(/,\s?/)
      .map((v) => v.replace("'", ''))
    labels = Array.from(new Set(labels))

    //datasets
    let datasets = new Array(labels.length).fill(0)
    this.value
      .slice(1, -1)
      .split(/,\s?/)
      .map((v) => v.replace("'", ''))
      .map((e) => {
        labels.map((l, i) => {
          if (l === e) datasets[i]++
        })
      })
  })
  $('.fq-select').on('input', function (e) {
    selectedValue = $('.fq-select option:selected').val()
    $(`.fq-box`).hide()
    $(`.fq-${selectedValue}`).show()
  })
})
