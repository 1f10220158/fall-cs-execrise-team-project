const pushFromData = document.getElementById('pushUserData');

pushFromData.addEventListener("submit", (event) =>{
    const userid = document.getElementById('userid');
    const password = document.getElementById('password');
    const userData = {
        "userid": userid,
        "password": password,
    };

    event.preventDefault();
    window.location.href = "{{% url index %}}";

    /* path= 'cookieが有効になる文書のパス'
    max-age= cookieの有効期限(秒)
    samesite= lax または strict (xsrf攻撃対策) */

    const path = '/';
    const maxAge = '60*60*24*30';
    const samesite = 'lax'; 
    document.cookie = "userid=" + userid 
                    + "; path=" + path
                    + "; max-age=" + maxAge
                    + "; samesite=" + samesite;
           
    document.cookie = "password=" + password 
                    + "; path=" + path
                    + "; max-age=" + maxAge
                    + "; samesite=" + samesite;
    
    fetch("{{% url storeCookie %}}", {
        method: "POST",
        header: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(userData)

    })
})
