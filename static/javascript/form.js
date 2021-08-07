$(function () {
  let currentPosition = parseInt($('.fm-quickmenu').css('top'))
  $(window).scroll(function () {
    let position = $(window).scrollTop()
    $('.fm-quickmenu')
      .stop()
      .animate({ top: position + currentPosition + 'px' }, 500)
  })
})
toastr.success('저장에 성공하였습니다.')
