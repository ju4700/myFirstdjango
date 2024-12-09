var translate = true;

$("#supportbtn").on('click', function () {
    hideAll();
    $("#support-sec").removeAttr("hidden");
});

$("#faqbtn").on('click', function () {
    hideAll();
    $("#faq-sec").removeAttr("hidden");
});

$("#detailsbtn").on('click', function () {
    hideAll();
    $("#details-sec").removeAttr("hidden");
});

$("#card").on('click', function () {
    hideAll();
    $("#card").addClass("optionsCard");
    $("#mobile").removeClass("optionsCard");
    $("#net").removeClass("optionsCard");
    $("#cards-sec").removeAttr("hidden");
});

$("#mobile").on('click', function () {
    hideAll();
    $("#mobile").addClass("optionsCard");
    $("#card").removeClass("optionsCard");
    $("#net").removeClass("optionsCard");
    $("#mobile-sec").removeAttr("hidden");
});

$("#net").on('click', function () {
    hideAll();
    $("#net").addClass("optionsCard");
    $("#card").removeClass("optionsCard");
    $("#mobile").removeClass("optionsCard");
    $("#netbank-sec").removeAttr("hidden");
});

$("#translatebtn").on('click', function () {
    translateAll();
});

function translateAll() {
    if (translate) {
        $("#support-text").attr("hidden", true);
        $("#bangla-support-text").removeAttr("hidden");

        $("#faq-support-text").attr("hidden", true);
        $("#bangla-faq-support-text").removeAttr("hidden");

        $("#translate-support-text").attr("hidden", true);
        $("#bangla-translate-support-text").removeAttr("hidden");

        $("#details-text").attr("hidden", true);
        $("#bangla-details-text").removeAttr("hidden");

        $("#cards-btn").attr("hidden", true);
        $("#bangla-cards-btn").removeAttr("hidden");

        $("#mobile-btn").attr("hidden", true);
        $("#bangla-mobile-btn").removeAttr("hidden");

        $("#support-content-title").attr("hidden", true);
        $("#bangla-support-content-title").removeAttr("hidden");

        $("#support-chat").attr("hidden", true);
        $("#bangla-support-chat").removeAttr("hidden");

        $("#support-mail").attr("hidden", true);
        $("#bangla-support-mail").removeAttr("hidden");

        $("#suport-call").attr("hidden", true);
        $("#bangla-suport-call").removeAttr("hidden");

        $("#faq-title-one").attr("hidden", true);
        $("#bangla-faq-title-one").removeAttr("hidden");

        $("#faq-details-one").attr("hidden", true);
        $("#bangla-faq-details-one").removeAttr("hidden");

        $("#faq-title-two").attr("hidden", true);
        $("#bangla-faq-title-two").removeAttr("hidden");

        $("#faq-details-two").attr("hidden", true);
        $("#bangla-faq-details-two").removeAttr("hidden");

        $("#faq-title-three").attr("hidden", true);
        $("#bangla-faq-title-three").removeAttr("hidden");

        $("#faq-details-three").attr("hidden", true);
        $("#bangla-faq-details-three").removeAttr("hidden");

        $("#trx-title").attr("hidden", true);
        $("#bangla-trx-title").removeAttr("hidden");

        $("#net-btn").attr("hidden", true);
        $("#bangla-net-btn").removeAttr("hidden");
    } else {
        $("#support-text").removeAttr("hidden");
        $("#bangla-support-text").attr("hidden", true);

        $("#faq-support-text").removeAttr("hidden");
        $("#bangla-faq-support-text").attr("hidden", true);

        $("#translate-support-text").removeAttr("hidden");
        $("#bangla-translate-support-text").attr("hidden", true);

        $("#details-text").removeAttr("hidden");
        $("#bangla-details-text").attr("hidden", true);

        $("#cards-btn").removeAttr("hidden");
        $("#bangla-cards-btn").attr("hidden", true);

        $("#mobile-btn").removeAttr("hidden");
        $("#bangla-mobile-btn").attr("hidden", true);

        $("#support-content-title").removeAttr("hidden");
        $("#bangla-support-content-title").attr("hidden", true);

        $("#support-chat").removeAttr("hidden");
        $("#bangla-support-chat").attr("hidden", true);

        $("#support-mail").removeAttr("hidden");
        $("#bangla-support-mail").attr("hidden", true);

        $("#suport-call").removeAttr("hidden");
        $("#bangla-suport-call").attr("hidden", true);

        $("#faq-title-one").removeAttr("hidden");
        $("#bangla-faq-title-one").attr("hidden", true);

        $("#faq-details-one").removeAttr("hidden");
        $("#bangla-faq-details-one").attr("hidden", true);

        $("#faq-title-two").removeAttr("hidden");
        $("#bangla-faq-title-two").attr("hidden", true);

        $("#faq-details-two").removeAttr("hidden");
        $("#bangla-faq-details-two").attr("hidden", true);

        $("#faq-title-three").removeAttr("hidden");
        $("#bangla-faq-title-three").attr("hidden", true);

        $("#faq-details-three").removeAttr("hidden");
        $("#bangla-faq-details-three").attr("hidden", true);

        $("#trx-title").removeAttr("hidden");
        $("#bangla-trx-title").attr("hidden", true);

        $("#net-btn").removeAttr("hidden");
        $("#bangla-net-btn").attr("hidden", true);
    }
    translate = !translate;
}

function hideAll() {
    $("#cards-sec").attr("hidden", true);
    $("#mobile-sec").attr("hidden", true);
    $("#support-sec").attr("hidden", true);
    $("#faq-sec").attr("hidden", true);
    $("#details-sec").attr("hidden", true);
    $("#netbank-sec").attr("hidden", true);
}