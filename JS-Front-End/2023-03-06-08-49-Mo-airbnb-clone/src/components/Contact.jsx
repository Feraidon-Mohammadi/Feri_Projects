import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEnvelope, faPhone } from "@fortawesome/free-solid-svg-icons";

// Object-Destructuring Syntax (extrahiert ausgewählte Properties aus einem Objekt und stellt sie als separate Variablen zur Verfügung)
// const { property1: alias, property2 = defaultValue, property3 } = anObject
// const { property1: { subProperty }, property2 } = anObject (anObject.property1.subProperty und anObject.property2)
export default function Contact({ name, phone, email, img: image }) {
  return (
    <div className="contact">
      <img src={image} className="contact__image" />
      <h1 className="contact__name">{name}</h1>
      <div className="contact__phone-details">
        <FontAwesomeIcon icon={faPhone} />
        <a className="contact__phone-number" href={`tel:${phone}`}>
          {phone}
        </a>
      </div>
      <div className="contact__mail-details">
        <FontAwesomeIcon icon={faEnvelope} />
        <a className="contact__mail-address" href={`mailto:${email}`}>
          {email}
        </a>
      </div>
    </div>
  );
}
