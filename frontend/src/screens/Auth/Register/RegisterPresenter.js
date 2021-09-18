import React from 'react'
import styled from "styled-components";
import Button, { SubmitButton } from "components/Auth/Button";
import Input from "components/Auth/Input";
import './register.css'


export const EmailWrapper = styled.div`
  display: flex;
  justify-content: space-around;
  align-items: center;
  width: 85%;
`;

export const EmailInput = styled.input`
background: rgba(255, 255, 255, 0.15);
box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
border-radius: 2rem;
width: 60%;
height: 3rem;
padding: 1rem;
border: none;
outline: none;
color: #3c354e;
font-size: 1rem;
color: #fff;
font-weight: bold;
&:focus {
  display: inline-block;
  box-shadow: 0 0 0 0.2rem #b9abe0;
  backdrop-filter: blur(12rem);
  border-radius: 2rem;
}
&::placeholder {
  color: #b9abe099;
  font-weight: 100;
  font-size: 1rem;
}
`;

export const EmailAuthBtn = styled.button`
  background: linear-gradient(to right, #14163c 0%, #03217b 79%);
  width: 30%;
  height: 3rem;
  border: none;
  color: white;
  border-radius: 2rem;
  cursor: pointer;
`;

export const RegisterContainer = styled.div`
    margin: auto;
    display: flex;
    align-items: center;
    flex-direction: column;
    height: 80vh;
    width: 35vw;
    background: rgba(255, 255, 255, 0.15);
    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    backdrop-filter: blur(8.5px);
    -webkit-backdrop-filter: blur(8.5px);
    border-radius: 10px;
    color: #ffffff;
    text-transform: uppercase;
    letter-spacing: 0.4rem;
    @media only screen and (max-width: 320px) {
    width: 80vw;
    height: 90vh;
    hr {
        margin-bottom: 0.3rem;
    }
    h4 {
        font-size: small;
    }
    }
    @media only screen and (min-width: 360px) {
    width: 80vw;
    height: 90vh;
    h4 {
        font-size: small;
    }
    }
    @media only screen and (min-width: 411px) {
    width: 80vw;
    height: 90vh;
    }
    @media only screen and (min-width: 768px) {
    width: 80vw;
    height: 80vh;
    }
    @media only screen and (min-width: 1024px) {
    width: 70vw;
    height: 50vh;
    }
    @media only screen and (min-width: 1280px) {
    width: 35vw;
    height: 80vh;
    }
`;

export const WelcomeText = styled.h2`
  margin: 3rem 0 2rem 0;
`;

export const InputContainer = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  height: 50%;
  width: 100%;
`;

export const ButtonContainer = styled.div`
  margin: 1rem 0 2rem 0;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
`;



export default function RegisterPresenter({ userName,
  setUserName,
  email,
  setEmail,
  password,
  setPassword,
  toggleAuthInput,
  onClick,
  handleSubmit }) {
  return (
    <div>
      <RegisterContainer>
        <WelcomeText>Register</WelcomeText>

        <InputContainer>
          <EmailWrapper>
            <EmailInput type="text" placeholder="Email" />
            <EmailAuthBtn onClick={onClick} >Check Email</EmailAuthBtn>
          </EmailWrapper>
          {toggleAuthInput && <Input type="text" placeholder="Active Code" />}

          <Input type="password" placeholder="Password" />
          <Input type="password" placeholder="Confirm Password" />
          <Input type="text" placeholder="Name" />
        </InputContainer>
        <ButtonContainer>
          <SubmitButton content="Register" fnc={handleSubmit} />
        </ButtonContainer>

      </RegisterContainer>

    </div>
  )
}