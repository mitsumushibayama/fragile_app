const nameform = document.getElementById('name');
const bikouform = document.getElementById('bikou');
const passform = document.getElementById('pass');
const register_button = document.getElementById('register_button');

register_button.addEventListener('click', () => {

    namevalue = nameform.value;
    bikouvalue = bikouform.value;
    passvalue = passform.value;

    if(namevalue != "" && bikouvalue != "" && passvalue != "") {

        const register_request = new XMLHttpRequest;

        let formdata = {
            'name': namevalue,
            'bikou': bikouvalue,
            'password': passvalue
        };

        //let data = {"formdata" : formdata }

        register_request.onreadystatechange = function () {

            if(this.readyState == 4 && this.status == 200) {

                console.log("リクエスト完了");
                const div = document.createElement('div');
                div.innerText = '登録が完了しました。';
                document.body.appendChild(div)
                response = this.response;
                console.log(response);

            }
            
        }
        const URL = '/post/user';
        register_request.open('POST', URL, true);
        register_request.setRequestHeader('Content-Type', 'application/json');
        register_request.responseType = 'json';
        register_request.send(JSON.stringify(formdata));

    }
    else {
        alert('必要な項目を入力してください');
    }

});