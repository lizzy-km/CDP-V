let နှိပ်ပါ = "click";
let အမဲပန်းအဖွဲ့ = [
  {
    id: "0",
    အမည်: "Lalisa",
  },
  {
    id: "1",
    အမည်: "Jennie Kim",
  },
  {
    id: "2",
    အမည်: "Kim Jisoo",
  },
  {
    id: "3",
    အမည်: "Park Chaeyoung",
  },
];

function သေတ္တာအသစ်ကိုဖန်တီးပါ(obj) {
  return document.createElement(obj);
}

function စာသားအသစ်ဖန်တီးပါ(text) {
  return document.createTextNode(text);
}

function သေတ္တာထဲသို့သေတ္တာအသစ်ထည့်ပါ(obj, innerObj) {
  return obj.appendChild(innerObj);
}

function အမည်ဖြင့်_စစ်ထုတ်ပါ(array, compareObj) {
  return array.filter((ar) =>
    ar.အမည်.toLowerCase().includes(compareObj.toLowerCase())
  );
}

function လုပ်ဆောင်ချက်ထည့်ပါ(obj) {
  return function (evn, func) {
    return obj.addEventListener(evn, func);
  };
}

let Idဖြင့်Elementကိုရယူပါ = (id) => document.getElementById(id);

const အဓိက = Idဖြင့်Elementကိုရယူပါ("အဓိက");
const ခန္ဓာကိုယ် = Idဖြင့်Elementကိုရယူပါ("ခန္ဓာကိုယ်");
const ခလုတ် = Idဖြင့်Elementကိုရယူပါ("ခလုတ်");

အဓိက.offsetWidth = ခန္ဓာကိုယ်?.offsetWidth;
အဓိက.offsetHeight = ခန္ဓာကိုယ်?.offsetHeight;

လုပ်ဆောင်ချက်ထည့်ပါ(ခလုတ်)(နှိပ်ပါ, () => {
  const စစ်ထုတ်ထားသော_အမည် = အမည်ဖြင့်_စစ်ထုတ်ပါ(အမဲပန်းအဖွဲ့, "lalisa").map(
    (အမဲပန်း) => အမဲပန်း.အမည်
  );
  const သေတ္တာ = သေတ္တာအသစ်ကိုဖန်တီးပါ("div");
  const စာသားအသစ် = စာသားအသစ်ဖန်တီးပါ(စစ်ထုတ်ထားသော_အမည်);
  သေတ္တာထဲသို့သေတ္တာအသစ်ထည့်ပါ(သေတ္တာ, စာသားအသစ်);
  သေတ္တာထဲသို့သေတ္တာအသစ်ထည့်ပါ(အဓိက, သေတ္တာ);
});
