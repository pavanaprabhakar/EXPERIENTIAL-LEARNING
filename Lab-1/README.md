# Remote Patient Vitals Alert & Monitoring App

A requirements engineering and UML modelling project for a remote patient monitoring system.

## 📌 Overview

The Remote Patient Vitals Alert & Monitoring App is designed to continuously monitor patient vital signs such as **SpO₂, heart rate, and blood pressure**.

The system evaluates incoming patient telemetry against configured clinical thresholds. When a critical anomaly is detected, the system generates an emergency alert and escalates it to the appropriate on-call caregiver.

## 🎯 Objective

The objective of this project is to:

- Identify functional and non-functional requirements.
- Define system behaviour using UML use-case modelling.
- Model the interaction between patients, telemetry devices, caregivers, and the monitoring system.
- Describe the process of generating and escalating emergency alerts.

## 👥 Actors

The system involves the following actors:

- **Remote Patient** – The patient whose vital signs are being monitored.
- **Telemetry Device** – Provides continuous patient vital readings to the system.
- **On-Call Caregiver** – Receives emergency alerts and views the patient's vital status.

## 🔄 System Workflow

```text
Patient Vital Telemetry
        ↓
Monitor Patient Vitals
        ↓
Evaluate Vital Thresholds
        ↓
Critical Anomaly Detected?
        ↓
Generate Emergency Alert
        ↓
Identify On-Call Caregiver
        ↓
Notify Caregiver
        ↓
Caregiver Views Patient Status