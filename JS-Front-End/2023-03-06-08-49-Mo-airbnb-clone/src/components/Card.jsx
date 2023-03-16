import imageUrl from "../assets/katie-zaferes.png";
import starUrl from "../assets/icons/star.png";

export default function Card(props) {
  return (
    <div className="card">
      <div className="card__image-details">
        <img src={props.img} className="card__image" />
        <div className="card__state-badge">{props.badge}</div>
      </div>
      <div className="card__stats">
        <img src={starUrl} className="card__rating-image" />
        <span className="card__rating">{props.rating}</span>
        <span className="card__rating-count">&#123;{props.reviewCount}&#125;</span>
        <span className="divider">·</span>
        <span className="card__location">{props.country}</span>
      </div>
      <p>
        <span className="card__title">{props.title}</span>
      </p>
      <p>
        <span className="card__price">From ${props.price}</span> / person
      </p>
    </div>
  );
}
