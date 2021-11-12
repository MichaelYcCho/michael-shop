import React, { useEffect} from 'react';

const Iamport = (order_data) => {

    useEffect(() => {
        const jquery = document.createElement('script');
        jquery.src = 'https://code.jquery.com/jquery-1.12.4.min.js';
        const iamport = document.createElement('script');
        iamport.src = 'https://cdn.iamport.kr/js/iamport.payment-1.1.7.js';
        document.head.appendChild(jquery);
        document.head.appendChild(iamport);

        return () => {
            document.head.removeChild(jquery);
            document.head.removeChild(iamport);
        }

}, [])


  const onSubmitIamport = (e) => {
      e.preventDefault();
        const {IMP} = window;
        IMP.init('imp56366274');
//order_data.totalPrice
    const data = {
            merchant_uid: `mid_${new Date().getTime()}`,
            pay_method: 'card',
            amount: 100,
            name: `${order_data.userName}의 결제`,
            buyer_name: order_data.userName,
            buyer_email: order_data.user_email,
            buyer_tel : order_data.phone,
        
    }

    IMP.request_pay(data, callback);
    }


    const callback = (response) => {
        const {success, error_msg, imp_uid, pay_method, paid_amount, status} = response
        if (success) {
            alert('성공');
            console.log(response);
        } else {
            alert(error_msg);
        }

    }

    return (
        <button type='submit' className="btn-hover" onClick={onSubmitIamport} >Place Order</button>
    )

}

export default Iamport;