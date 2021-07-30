const reference_button = document.getElementById("reference_button");
const message = document.getElementById("msg");

reference_button.addEventListener('click', () => {

    const idbox = document.getElementById("reference_id");
    const passwordbox = document.getElementById("pass");
    const idvalue = idbox.value;
    const passvalue = passwordbox.value;

    if(idvalue != "" && passvalue != "") {

        const PassCheckrequest = new XMLHttpRequest;
        PassCheckrequest.onreadystatechange = function () {
            if(this.readyState == 4 && this.status == 200) {
                const response = this.response;
                ans = response.user_pass[0].pass;
                if(passvalue == ans) {

                    console.log('Yes!');
                    const request = new XMLHttpRequest();
                    request.onreadystatechange = function() {
                        if(this.readyState == 4 && this.status == 200) {
                            console.log('DONE:リクエスト完了');
                            const responses = this.response;
                            let div = document.createElement('div');
                            div.innerText = 'userID: ' + responses.id_user[0].id + '  name: ' + responses.id_user[0].name;
                            document.body.appendChild(div)
                        }
                    }
                    const URL = '/get/user/' + idvalue;
                    request.open('GET', URL, true);
                    request.responseType = 'json';
                    request.send();    
                }
                else {
                    console.log('No!');
                }

            }
        }
        const pcURL = 'get/user/' + idvalue + '/pass';
        PassCheckrequest.open('GET', pcURL, true);
        PassCheckrequest.responseType = 'json';
        PassCheckrequest.send();
    }
    else if(idvalue == "" && passvalue == "") {
        const div = document.createElement('div');
        div.innerText = 'IDとパスワードを入力してください';
        document.body.appendChild(div)
    }
    else if(idvalue == "") {
        const div = document.createElement('div');
        div.innerText = 'IDを入力してください';
        document.body.appendChild(div)
    }
    else {
        const div = document.createElement('div');
        div.innerText = 'パスワードを入力してください';
        document.body.appendChild(div)
    }
});