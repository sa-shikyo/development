# -*- coding: utf-8 -*-


def captions(func):
    """
    画面要素のタイトル (デコレータ)
    """
    def _wrapped_view_func(request, *args, **kwargs):
        # logger.debug(u'-----------------------------------')
        # logger.debug(u'company_captions - args:   %s' % str(args))
        # logger.debug(u'company_captions - kwargs: %s' % str(kwargs))
        # logger.debug(u'-----------------------------------')

            try:

                lcid = request.session.get('_language', getattr(settings, "LANGUAGE_CODE", "ja"))
                # -------------------------
                # caption情報を取得
                # -------------------------
                caption_info = 

                request.captions = caption_info


        return func(request, *args, **kwargs)

    return _wrapped_view_func
