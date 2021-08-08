$(function () {
  pieInputs = $('.fm-pieVal')
  pieInputs.map(function (i) {
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

    //colors
    let colors = []
    let getRandomColor = function () {
      let r = Math.floor(Math.random() * 255)
      let g = Math.floor(Math.random() * 255)
      let b = Math.floor(Math.random() * 255)
      return 'rgb(' + r + ',' + g + ',' + b + ')'
    }
    for (var i in labels) {
      colors.push(getRandomColor())
    }

    let ctx = $(`#${this.name}`)[0].getContext('2d')

    var pie = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: labels,
        datasets: [
          {
            data: datasets,
            backgroundColor: colors,
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'right',
          },
          title: {
            display: false,
          },
        },
      },
    })
  })
})
