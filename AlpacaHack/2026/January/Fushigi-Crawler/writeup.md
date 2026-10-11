# 問題URL

https://alpacahack.com/challenges/fushigi-crawler

# 問題文

クローラーからのアクセスが変らしい！

# writeup

index.js 16行目
```js
    const r = await fetch(url, { headers: { FLAG }, signal: AbortSignal.timeout(5000) }); // !!
```

headerにそのまま `FLAG` を入れているので、これを見ればいい。

自作のサーバーとかは持ち合わせていないので、webhook.site というサイトを利用させてもらいました。ありがとうございます！

参考url: [webhook.siteさん](https://www.google.com/search?q=webhook.site+%E3%81%A8%E3%81%AF&oq=webhook.site+%E3%81%A8%E3%81%AF&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABiABBiiBNIBCDMxNzhqMGo3qAIIsAIB8QVtKg2SAP5DXg&sourceid=chrome&source=chrome.ob&ie=UTF-8#:~:text=%E5%85%AC%E5%BC%8F%E3%82%B5%E3%82%A4%E3%83%88%EF%BC%9A-,Webhook.site,-%E4%B8%BB%E3%81%AA%E7%89%B9%E5%BE%B4)
