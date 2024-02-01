!(function () {
  "use strict";
  var e,
    t,
    n,
    r,
    o,
    i,
    u = {},
    a = {};
  function c(e) {
    var t = a[e];
    return (
      void 0 !== t ||
        ((t = a[e] =
          {
            id: e,
            loaded: !1,
            exports: {},
          }),
        u[e].call(t.exports, t, t.exports, c),
        (t.loaded = !0)),
      t.exports
    );
  }
  function l(e) {
    return new Promise(function (t, n) {
      var r = c.miniCssF(e),
        o = c.p + r;
      if (
        (function (e, t) {
          for (
            var n = document.getElementsByTagName("link"), r = 0;
            r < n.length;
            r++
          ) {
            var o =
              (i = n[r]).getAttribute("data-href") || i.getAttribute("href");
            if ("stylesheet" === i.rel && (o === e || o === t)) return i;
          }
          var i,
            u = document.getElementsByTagName("style");
          for (r = 0; r < u.length; r++)
            if ((o = (i = u[r]).getAttribute("data-href")) === e || o === t)
              return i;
        })(r, o)
      )
        return t();
      var i = e,
        u = o,
        a = t,
        l = n,
        f = document.createElement("link");
      (f.rel = "stylesheet"),
        (f.type = "text/css"),
        (f.onerror = f.onload =
          function (e) {
            var t, n;
            (f.onerror = f.onload = null),
              "load" === e.type
                ? a()
                : ((t = e && ("load" === e.type ? "missing" : e.type)),
                  (e = (e && e.target && e.target.href) || u),
                  ((n = new Error(
                    "Loading CSS chunk " + i + " failed.\n(" + e + ")"
                  )).code = "CSS_CHUNK_LOAD_FAILED"),
                  (n.type = t),
                  (n.request = e),
                  f.parentNode.removeChild(f),
                  l(n));
          }),
        (f.href = u),
        document.head.appendChild(f);
    });
  }
  function f(e, t) {
    var n,
      r,
      i,
      u = t[0],
      a = t[1],
      l = t[2],
      f = 0;
    if (
      u.some(function (e) {
        return 0 !== o[e];
      })
    ) {
      for (n in a) c.o(a, n) && (c.m[n] = a[n]);
      l && (i = l(c));
    }
    for (e && e(t); f < u.length; f++)
      (r = u[f]), c.o(o, r) && o[r] && o[r][0](), (o[r] = 0);
    return c.O(i);
  }
  (c.m = u),
    (e = []),
    (c.O = function (t, n, r, o) {
      if (!n) {
        for (var i = 1 / 0, u = 0; u < e.length; u++) {
          (n = e[u][0]), (r = e[u][1]), (o = e[u][2]);
          for (var a, l = !0, f = 0; f < n.length; f++)
            (!1 & o || o <= i) &&
            Object.keys(c.O).every(function (e) {
              return c.O[e](n[f]);
            })
              ? n.splice(f--, 1)
              : ((l = !1), o < i && (i = o));
          l && (e.splice(u--, 1), void 0 !== (a = r()) && (t = a));
        }
        return t;
      }
      o = o || 0;
      for (u = e.length; 0 < u && e[u - 1][2] > o; u--) e[u] = e[u - 1];
      e[u] = [n, r, o];
    }),
    (c.n = function (e) {
      var t =
        e && e.__esModule
          ? function () {
              return e.default;
            }
          : function () {
              return e;
            };
      return (
        c.d(t, {
          a: t,
        }),
        t
      );
    }),
    (c.d = function (e, t) {
      for (var n in t)
        c.o(t, n) &&
          !c.o(e, n) &&
          Object.defineProperty(e, n, {
            enumerable: !0,
            get: t[n],
          });
    }),
    (c.f = {}),
    (c.e = function (e) {
      return Promise.all(
        Object.keys(c.f).reduce(function (t, n) {
          return c.f[n](e, t), t;
        }, [])
      );
    }),
    (c.u = function (e) {
      return (
        "js/" +
        e +
        "." +
        {
          284: "255f1cfc",
          323: "762b48b7",
          330: "281263c1",
          653: "ac95decb",
          963: "7dc58050",
        }[e] +
        ".js"
      );
    }),
    (c.miniCssF = function (e) {
      return (
        "css/" +
        e +
        "." +
        {
          284: "a2a097e1",
          323: "89e1586b",
          653: "e14110f2",
          963: "4fe21eda",
        }[e] +
        ".css"
      );
    }),
    (c.g = (function () {
      if ("object" == typeof globalThis) return globalThis;
      try {
        return this || new Function("return this")();
      } catch (i) {
        if ("object" == typeof window) return window;
      }
    })()),
    (c.o = function (e, t) {
      return Object.prototype.hasOwnProperty.call(e, t);
    }),
    (t = {}),
    (n = "SimpleTex:"),
    (c.l = function (e, r, o, i) {
      if (t[e]) t[e].push(r);
      else {
        var u, a;
        if (void 0 !== o)
          for (
            var l = document.getElementsByTagName("script"), f = 0;
            f < l.length;
            f++
          ) {
            var d = l[f];
            if (
              d.getAttribute("src") == e ||
              d.getAttribute("data-webpack") == n + o
            ) {
              u = d;
              break;
            }
          }
        u ||
          ((a = !0),
          ((u = document.createElement("script")).charset = "utf-8"),
          (u.timeout = 120),
          c.nc && u.setAttribute("nonce", c.nc),
          u.setAttribute("data-webpack", n + o),
          (u.src = e)),
          (t[e] = [r]);
        r = function (n, r) {
          (u.onerror = u.onload = null), clearTimeout(s);
          var o = t[e];
          if (
            (delete t[e],
            u.parentNode && u.parentNode.removeChild(u),
            o &&
              o.forEach(function (e) {
                return e(r);
              }),
            n)
          )
            return n(r);
        };
        var s = setTimeout(
          r.bind(null, void 0, {
            type: "timeout",
            target: u,
          }),
          12e4
        );
        (u.onerror = r.bind(null, u.onerror)),
          (u.onload = r.bind(null, u.onload)),
          a && document.head.appendChild(u);
      }
    }),
    (c.r = function (e) {
      "undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, {
          value: "Module",
        }),
        Object.defineProperty(e, "__esModule", {
          value: !0,
        });
    }),
    (c.nmd = function (e) {
      return (e.paths = []), e.children || (e.children = []), e;
    }),
    (c.p = "/"),
    (r = {
      666: 0,
    }),
    (c.f.miniCss = function (e, t) {
      r[e]
        ? t.push(r[e])
        : 0 !== r[e] &&
          {
            284: 1,
            323: 1,
            653: 1,
            963: 1,
          }[e] &&
          t.push(
            (r[e] = l(e).then(
              function () {
                r[e] = 0;
              },
              function (t) {
                throw (delete r[e], t);
              }
            ))
          );
    }),
    (o = {
      666: 0,
    }),
    (c.f.j = function (e, t) {
      var n,
        r,
        i = c.o(o, e) ? o[e] : void 0;
      0 !== i &&
        (i
          ? t.push(i[2])
          : 666 != e
          ? ((n = new Promise(function (t, n) {
              i = o[e] = [t, n];
            })),
            t.push((i[2] = n)),
            (t = c.p + c.u(e)),
            (r = new Error()),
            c.l(
              t,
              function (t) {
                var n;
                c.o(o, e) &&
                  (0 !== (i = o[e]) && (o[e] = void 0),
                  i &&
                    ((n = t && ("load" === t.type ? "missing" : t.type)),
                    (t = t && t.target && t.target.src),
                    (r.message =
                      "Loading chunk " +
                      e +
                      " failed.\n(" +
                      n +
                      ": " +
                      t +
                      ")"),
                    (r.name = "ChunkLoadError"),
                    (r.type = n),
                    (r.request = t),
                    i[1](r)));
              },
              "chunk-" + e,
              e
            ))
          : (o[e] = 0));
    }),
    (c.O.j = function (e) {
      return 0 === o[e];
    }),
    (i = self.webpackChunkSimpleTex = self.webpackChunkSimpleTex || []).forEach(
      f.bind(null, 0)
    ),
    (i.push = f.bind(null, i.push.bind(i)));
})();
