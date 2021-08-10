$(function () {
  $(`.fq-1`).show()

  $('.fq-select').on('input', function (e) {
    selectedValue = $('.fq-select option:selected').val()
    $(`.fq-box`).hide()
    $(`.fq-${selectedValue}`).show()
  })

  $('.fr-down').click(function (e) {
    toastr.success('성공적으로 다운로드 하였습니다.')
  })
})
